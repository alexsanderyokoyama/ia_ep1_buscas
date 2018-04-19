# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
 
    # Pilha de nos
    pilha = util.Stack()
    # Array de coordenadas ja visitadas
    coordVisitados = []
    # No de inicio  (coordenada do no, direcao, caminho percorrido ate este no)
    noInicial = (problem.getStartState(), None, [])
    # Insere o primeiro inicial na lista de nos
    pilha.push(noInicial) 
    
    # Itera ate que a pilha esteja vazia
    while not pilha.isEmpty():
        atual = pilha.pop()                         # Remove o no do topo da pilha 
        atualCoord = atual[0]                       # Guarda a coordenada do no atual
        # atualAcao = atual[1]                        # Guarda a acao (direcao) pela qual se chegou no no atual
        atualCaminho = atual[2]                     # Guarda o caminho ate ter chegado neste no atual
        if(atualCoord not in coordVisitados):       # Se o no atual ainda nao foi visitado, continuar
            coordVisitados.append(atualCoord)       # Adiciona a coord do atual na lista de visitados
            if(problem.isGoalState(atualCoord)):    # Se eh o objetivo, retorna o caminho ate chegar neste no
				return atualCaminho 
            sucessores = problem.getSuccessors(atualCoord)  # Encontrar todos os nos vizinhos
            for sucessor in sucessores:                     # Expande os nos vizinhos, na sequencia da lista
                if sucessor[0] not in coordVisitados:       # Se o vizinho ainda nao foi visitado, coloca na lista
                    pilha.push((sucessor[0], sucessor[1], atualCaminho + [sucessor[1]]))
    return[]

  
# Igual o depthFirstSearch, porem utilizando Fila em vez de Pilha
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # Fila de nos
    fila = util.Queue()
    # Array de coordenadas ja visitadas
    coordVisitados = []
    # No de inicio  (coordenada do no, direcao, caminho percorrido ate este no)
    noInicial = (problem.getStartState(), None, [])
    # Insere o primeiro inicial na lista de nos
    fila.push(noInicial) 
    
    # Itera ate que a fila esteja vazia
    while not fila.isEmpty():
        atual = fila.pop()                         # Remove o no do topo da fila 
        atualCoord = atual[0]                       # Guarda a coordenada do no atual
        # atualAcao = atual[1]                        # Guarda a acao (direcao) pela qual se chegou no no atual
        atualCaminho = atual[2]                     # Guarda o caminho ate ter chegado neste no atual
        if(atualCoord not in coordVisitados):       # Se o no atual ainda nao foi visitado, continuar
            coordVisitados.append(atualCoord)       # Adiciona a coord do atual na lista de visitados
            if(problem.isGoalState(atualCoord)):    # Se eh o objetivo, retorna o caminho ate chegar neste no
				return atualCaminho 
            sucessores = problem.getSuccessors(atualCoord)  # Encontrar todos os nos vizinhos (sucessores)
            for sucessor in sucessores:              # Expande os nos vizinhos, na sequencia da lista
                if sucessor[0] not in coordVisitados:       # Se o vizinho ainda nao foi visitado, coloca na lista
                    fila.push((sucessor[0], sucessor[1], atualCaminho + [sucessor[1]]))
    return[]

    
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # Define a funcao que define os custos da lista de acoes 
    def ordenaCustos(caminho):
        acoes = [] # Cria lista de acoes
        if caminho is None:
            return # Retorna se caminho estiver vazio (estado inicial)
        acoes = list(caminho[2]) # Clona lista de acoes do caminho
        return problem.getCostOfActions(acoes) # Retorna lista de custos das acoes

    # Armazena funcao de custos em um callback para ser utilizado na fila de prioridade
    callback = ordenaCustos

    # Initializa fila de prioridade com o callback
    filaPrioridade = util.PriorityQueueWithFunction(callback)

    # Array de coordenadas ja visitadas
    coordVisitados = []
    # No de inicio  (coordenada do no, direcao, caminho percorrido ate este no)
    noInicial = (problem.getStartState(), None, [])
    # Insere o primeiro inicial na lista de nos
    filaPrioridade.push(noInicial) 
    
    # Itera ate que a fila esteja vazia
    while not filaPrioridade.isEmpty():
        atual = filaPrioridade.pop()                         # Remove o no do topo da fila 
        atualCoord = atual[0]                       # Guarda a coordenada do no atual
        # atualAcao = atual[1]                        # Guarda a acao (direcao) pela qual se chegou no no atual
        atualCaminho = atual[2]                     # Guarda o caminho ate ter chegado neste no atual
        if(atualCoord not in coordVisitados):       # Se o no atual ainda nao foi visitado, continuar
            coordVisitados.append(atualCoord)       # Adiciona a coord do atual na lista de visitados
            if(problem.isGoalState(atualCoord)):    # Se eh o objetivo, retorna o caminho ate chegar neste no
				return atualCaminho 
            sucessores = problem.getSuccessors(atualCoord)  # Encontrar todos os nos vizinhos (sucessores)
            for sucessor in sucessores:              # Expande os nos vizinhos, na sequencia da lista
                if sucessor[0] not in coordVisitados:       # Se o vizinho ainda nao foi visitado, coloca na lista
                    filaPrioridade.push((sucessor[0], sucessor[1], atualCaminho + [sucessor[1]]))
    return[]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def learningRealTimeAStar(problem, heuristic=nullHeuristic):
    """Execute a number of trials of LRTA* and return the best plan found."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    # MAXTRIALS = ...
    

# Abbreviations 
# *** DO NOT CHANGE THESE ***
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
lrta = learningRealTimeAStar
