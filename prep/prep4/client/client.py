import xmlrpc.client
import random
import visualizer
import xml.etree.ElementTree as ET

class Agent:
    def __init__(self, filename):   
        tree = ET.parse(filename)
        root = tree.getroot()
        
        self.login = root.find('login').text
        self.data = []
        self.visualizer = visualizer.Visualizer()
        self.gameserver = xmlrpc.client.ServerProxy(root.find('url').text)
        self.gameserver.add_player(self.login)

    def action(self):
        self.gameserver.make_action(str(self.login), 'look', '')
        self.visualizer.visualize(self.data)

    def __repr__(self):
        return str(self.data)

    def save_data(self):
        with open('data.txt', 'w') as f:
            f.write(self.__repr__())    

class AgentRandom(Agent):
    def action(self):
        directions = ['north', 'west', 'south', 'east']
        random_direction = random.choice(directions)
        result = self.gameserver.make_action(self.login, 'move', random_direction)
        self.visualizer.visualize(result)

class AgentLeftRight(Agent):
    def __init__(self, filename):
        super().__init__(filename)
        self.direction = 'west'

    def action(self):
        if len(self.data) > 5 and len(self.data[5]) > 5:
            barrier = self.data[5][4] if self.direction == 'west' else self.data[5][6]
            if barrier in ['t', 'o', '~']:
                self.direction = 'east' if self.direction == 'west' else 'west'
        self.data = self.gameserver.make_action(self.login, 'move', self.direction)
        self.visualizer.visualize(self.data)

def main():
    agent = None
    try:
        agent = AgentLeftRight('config.xml')
        while agent.visualizer.running:
            agent.action()
            print(agent)
        else:
            agent.gameserver.make_action(agent.login, 'exit', '')
        agent.save_data()
    except KeyboardInterrupt:
        agent.gameserver.make_action(agent.login, 'exit', '')

if __name__ == '__main__':
    main()