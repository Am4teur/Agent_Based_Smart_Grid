import settings 
import map
import charger_handler,driver_assistant,energy_broker,power_operative, geographic_agent
import random
import time
import threading
import numpy as np
import networkx as nx
import settings
from PyQt5.QtCore import QEventLoop
from PyQt5.QtCore import QTimer
from matplotlib import pyplot as plt
import statistics
from numpy import zeros


class simulation():

    def test(self,map1,gui):
        self.start_simulation(map1,gui)

        da_list = []
        aux_priori = self.number_priority_vehicles
        for i in range(self.number_vehicles):
            #lng, lat = map1.get_random_point()
            rand_bat = random.uniform(self.standard_batery_size* 0.6, self.standard_batery_size)
            rand_chaged = random.uniform(rand_bat* 0.6, rand_bat)
            A,route  = self.generate_route()
            if (aux_priori>0):
                aux_priori-= 1
                is_priority = True
            else:
                is_priority = False
            time_u = random.uniform(0,1)
            price_u = random.uniform(0,1)
            distance_u = random.uniform(0,1)
            c = driver_assistant.driver_assistant(A, route, rand_chaged, rand_bat, settings.max_battery, settings.battery_percentage_spend_per_tick, map1, is_priority,i, time_u, price_u, distance_u, self)
            self.agent_list.append(c)
            da_list.append(c)
        
        ch_list = []
        for i in range(self.number_stations):
            lng, lat = map1.get_random_point()
            cost_tick = settings.cost_per_tick * random.uniform(0.6,1)
            b = charger_handler.charger_handler(lat,lng, map1, self.energy_price_buy, self.energy_price_sell, i, self, cost_tick, settings.charger_flow)
            self.agent_list.append(b)
            ch_list.append(b)
        
        for i in range(self.number_vehicles):
            da_list[i].init_ch_list(ch_list)
        
        lng, lat = map1.get_random_point()
        d = power_operative.power_operative(lat,lng, self.storage_available, self)
        self.agent_list.append(d)
        self.po = d

        #lng, lat = map1.get_random_point()
        a = energy_broker.energy_broker(settings.point[0],settings.point[1],self.step_of_disaster,self.total_energy_of_tick, self.total_evergy_of_simulation, self,  self.step_of_redistribuition, self.max_flactuation, self.min_flactuation)
        self.agent_list.append(a)
        self.eb = a

        map1.add_agents(self.agent_list)
        for agent in self.agent_list:
            if agent.name != "power operative":
                self.proactive_agents.append(agent)
        
        while self.current_step < self.steps:
        #for current_step in range(self.steps):
            if not self.stop_tog or self.do_step_arg:
                for agent in self.proactive_agents:
                    agent.act()
                #c.animate()
            self.update(gui)
        self.end(gui)  
        self.graph()
                   
    def One_DA_N_CH(self,N):
        self.architecture = "1 DA; N CH; 1 PO; 1 EB"
        pass

    def N_DA_N_CH(self,map1,gui):
        self.architecture = "N DA; N CH; 1 PO; 1 EB"

        gui.disp_vehicles.setText(str(self.number_vehicles))
        gui.disp_stations.setText(str(self.number_stations))
        gui.disp_priority.setText(str(self.number_priority_vehicles))
        listToStr = ' '.join([str(elem) for elem in self.step_of_disaster])
        gui.disp_outages.setText(str(self.number_disasters)+" in ticks: "+listToStr)
        self.agent_list = []
        aux_priori = self.number_priority_vehicles
        for i in range(self.number_vehicles):
            lng, lat = map1.get_random_point()
            rand_bat = random.uniform(self.standard_batery_size* 0.6, self.standard_batery_size)
            if (aux_priori>0):
                aux_priori-= 1
                c = driver_assistant.driver_assistant(lat,lng, rand_bat)
                # this has to have priority
            
            c = driver_assistant.driver_assistant(lat,lng, rand_bat)
            self.agent_list.append(c)

        for i in range(self.number_stations):
            lng, lat = map1.get_random_point()
            c = charger_handler.charger_handler(lat,lng, map1)
            self.agent_list.append(c)

        lng, lat = map1.get_random_point()
        eb = energy_broker.energy_broker(lat,lng)
        lng, lat = map1.get_random_point()
        po = power_operative.power_operative(lat,lng)
        self.agent_list.append(eb)
        self.agent_list.append(po)
       
        map1.add_agents(self.agent_list)
        self.curret_step = 0
        
        for curret_step in range(self.steps):

            for agent in self.agent_list:
                agent.act()










            update(current_step,gui)
            
        gui.disp_time.setText("Complete")

    def One_DA_One_CH(self, N):
        self.architecture = "1 DA; 1 CH; 1 PO; 1 EB"
        pass

    def N_DA_One_CH(self,N):
        self.architecture = "N DA; 1 CH; 1 PO; 1 EB"
        pass

    def stop(self):
        if not self.stop_tog:
            self.stop_tog = True
        else:
            self.stop_tog = False

    def __init__(self):
        self.stop_tog = False
        self.steps = settings.simulation_time
        self.number_vehicles = settings.nr_vehicles
        self.number_priority_vehicles = settings.nr_priority_vehicles #random.choice(range(self.number_vehicles)) #7
        self.number_stations = settings.nr_stations
        self.number_disasters = settings.nr_disasters  #to generate the disaster pick an int between 0 and number of stepps
        self.step_of_disaster = []# we have to generate the impact of the disaster randomly
        self.number_redistribuition = settings.nr_redistribution  #to generate the redistribuition pick an int between 0 and number of stepps
        self.step_of_redistribuition = []# we have to generate the impact of the redistribuition randomly
        self.max_flactuation = settings.max_source_flactuation # if we put min and max equal the flactuation is the same every time
        self.min_flactuation = settings.min_source_flactuation
        self.standard_batery_size = settings.standard_batery_size # this can flactuate per car
        self.total_energy_of_tick = settings.total_energy_of_tick #self.number_vehicles*self.standard_batery_size
        self.total_evergy_of_simulation = settings.total_evergy_of_simulation#self.steps*self.total_energy_of_tick 
        tick_range = []
        if self.number_disasters>0 or self.number_redistribuition>0:
            for i in range(self.steps):
                tick_range.append(i) 
            self.step_of_disaster = random.sample(tick_range, self.number_disasters)
            print(self.step_of_disaster)

            for i in range(self.steps):
                tick_range.append(i) 
            self.step_of_redistribuition = random.sample(tick_range, self.number_redistribuition)
            print(self.step_of_redistribuition)
        print(self.number_priority_vehicles)
        self.step_of_disaster.sort()
        self.step_of_redistribuition.sort()

        self.step_time_sec = settings.step_time_milisec
        self.agent_list = []
        self.proactive_agents =[]
        #storage available for PO
        self.storage_available = settings.storage_available
        self.energy_price_buy = settings.energy_price_buy
        self.energy_price_sell = settings.energy_price_sell
        self.current_step = 0
        self.prev_step = -1
        self.architecture = settings.architecture
        self.map1 = None
        self.po = None
        self.eb = None

        #stats for simulation results
        self.po_power =[]
        self.number_of_inactive_stations = []
        self.time_to_charge_worst_case =[]
        ##must add method calculate time to charge in DA
        self.number_comunications = []
        #has values per each tick/step
        self.energy_history = []

        self.cost_of_system = []
        self.revenue_of_system = []
        self.profit = [] #costof mantaining vs money made
        self.number_cars_charging =[]
        self.number_cars_without_energy = []
         
        #get_time_of_wait
        
   

        

        pass

    def start_simulation(self,map1,gui):
        #self.architecture = "Test"
        
        self.current_step = 0
        #c = geographic_agent.geographic_agent(38.7414116,-9.143627785022142)
        #print(b.get_latitude())
        gui.disp_architecture.setText(settings.architecture)
        gui.disp_vehicles.setText(str(self.number_vehicles))
        gui.disp_stations.setText(str(self.number_stations))
        gui.disp_priority.setText(str(self.number_priority_vehicles))
        map1.clean_map()
        listToStr = ' '.join([str(elem) for elem in self.step_of_disaster])
        gui.disp_outages.setText(str(self.number_disasters)+" next: "+listToStr)
        self.agent_list = []
        self.map1 = map1

        self.po_power =[]
        self.number_of_inactive_stations = []
        self.time_to_charge_worst_case =[]
        ##must add method calculate time to charge in DA
        self.number_comunications = []
        #has values per each tick/step
        self.energy_history = []

        self.cost_of_system = []
        self.revenue_of_system = []
        self.profit = [] #costof mantaining vs money made

        self.number_cars_charging =[]
        self.number_cars_without_energy = []
        self.accumulated_profit = []



        for i in range(self.steps):
            self.cost_of_system.append(0)
            self.revenue_of_system.append(0)
            self.profit.append(0)

            self.number_cars_charging.append(0)
            self.number_cars_without_energy.append(0)
            self.accumulated_profit.append(0)
            
            self.number_of_inactive_stations.append(self.number_stations)
            aux = []
            for j in range(self.number_stations ):
                aux.append(0)
            self.time_to_charge_worst_case.append(aux)   
            

    def do_step(self):
        self.do_step_arg = True
        pass

    def update(self, gui):
        loop = QEventLoop()
        QTimer.singleShot(self.step_time_sec, loop.quit)
        loop.exec_()
        if not self.stop_tog or self.do_step_arg:
            self.current_step += 1
            print('#########  '+str(self.current_step)+'  #########')
            
        #self.current_step = current_step
        
        if (not self.stop_tog or self.do_step_arg) and self.prev_step != self.current_step:
            self.prev_step = self.current_step
            gui.disp_time.setText(str(self.current_step))

           

            #self.po_power.append[self.po.]
            if self.current_step in self.step_of_disaster:
                listToStr = ' '.join([str(elem) for elem in self.step_of_disaster])
                gui.disp_outages.setText(str(self.number_disasters)+" next: "+listToStr)

            if self.current_step in self.step_of_redistribuition:
                listToStr = ' '.join([str(elem) for elem in self.step_of_redistribuition])
                gui.disp_redistribution.setText(str(self.number_redistribuition)+" next: "+listToStr)
            gui.disp_architecture.setText(self.architecture)

            if self.current_step <len(self.number_cars_charging):
                gui.disp_car_charging.setText(str(self.number_cars_charging[self.current_step]))
                gui.disp_worst_time.setText(str(max(self.time_to_charge_worst_case[self.current_step])))
                gui.disp_car_wo_energy.setText(str(self.number_cars_without_energy[self.current_step]))

            try:
                gui.disp_po_energy.setText(str(self.po_power[-1]))
            except:
               gui.disp_po_energy.setText("po_desconhecido")
           
            gui.reload_map()
            self.do_step_arg = False

    def end(self, gui):
        gui.disp_time.setText("Complete")
        print("Complete")

    def plot(self,x,y, disc_x, disc_y):
        fig_energy, ax_energy = plt.subplots()
        #xerr = 5000*np.random.random_sample(20)
        #my_xticks = ['a', 'b', 'c', 'd']
        #plt.xticks(x, x)
        yerr = (statistics.mean(y) /10)*np.random.random_sample(len(y))
        ax_energy.errorbar(x, y,yerr=yerr,fmt='-o',marker='s', mfc='blue',
         mec='green',  ecolor='r')
        plt.axis([0, max(x), 0, (max(y)+max(yerr))])
        plt.ylabel(disc_y)
        plt.xlabel(disc_x)
        #plt.show()
        plt.savefig('graphs/'+str(self.graph_n)+'.png')
        self.graph_n +=1

    def graph(self):
        self.graph_n = 0
        #print(self.number_of_inactive_stations)
        self.plot(list(range(self.steps)), self.number_of_inactive_stations,'Step', 'Number of Inactive Stations')
        #print(self.po_power)
        self.plot(list(range(self.steps)), self.po_power,'Step', 'Energy available from Power Operative')
        #print(self.time_to_charge_worst_case)
        aux_worst_list = []
        for i in self.time_to_charge_worst_case:
            aux_worst_list.append(max(i))
        #print('revenue')
        #print(self.revenue_of_system)
        #print('cost')
        #print(self.cost_of_system)
        for i in range(self.steps):
            self.profit [i] = (self.revenue_of_system[i]*(1-settings.tax))-self.cost_of_system[i]
        #print(self.profit)
        self.plot(list(range(self.steps)), self.profit,'Step', 'Profit after Tax')
        
        
        for i in range(len(self.profit)):
            if i == 0:
                self.accumulated_profit[i] += self.profit[i]
            else:
                for j in range(i):
                    self.accumulated_profit[i] += self.profit[j]
        self.plot(list(range(self.steps)), self.accumulated_profit,'Step', 'Accumulated profit after Tax')
        self.plot(list(range(self.steps)), aux_worst_list,'Step', 'Worst time to wait')

        self.plot(list(range(self.steps)), self.number_cars_charging,'Step', 'Number of cars charging')
        self.plot(list(range(self.steps)), self.number_cars_without_energy,'Step', 'Number of cars with dead battery')
        for agent in self.agent_list:
            if agent.name == "energy broker":
                self.energy_history = agent.energy_history
                print(len(self.energy_history))
                self.plot(list(range(self.steps)), self.energy_history,'Step', 'Energy available from Energy Broker')
                
                break
            else:
                self.energy_history = "energy_history not found"
        
    def generate_route(self):
        #DRIVER ASSISTANT
        #Generate a route -> TODO: Have a function that do this
        route = []
        no_route = True
        A = None
        while no_route:
            try:
                # A->B
                A = np.random.choice(self.map1.G.nodes)
                B = np.random.choice(self.map1.G.nodes)
                r = nx.shortest_path(self.map1.G, A, B, weight='length')
                route.append(r)

                # B->C
                C = np.random.choice(self.map1.G.nodes)
                r = nx.shortest_path(self.map1.G, B, C, weight='length')
                route.append(r)

                # C->A
                r = nx.shortest_path(self.map1.G, C, A, weight='length')
                route.append(r)

                no_route = False
            except:
                print("Route couldn't be created.... Retrying")    
        return A , route


