library(igraph)
g <- make_graph('Diamond') %>%
  set_vertex_attr('name', value = LETTERS[1:4]) %>%
  add_layout_(with_fr()) %>%
  plot()

library(igraphdata)
data(package = 'igraphdata')

data("macaque")
macaque

gorder(macaque) #number of vertex
gsize(macaque) #number of edges
V(macaque)
E(macaque)
macaque %>% ends('V1|V2')
macaque %>% tail_of('V1|V2')
macaque %>% head_of('V1|V2')
macaque %>% neighbors('PIP', mode = 'out')
macaque %>% head_of('PIP|V2')
macaque %>% neighbors('PIP', mode = 'in')

V(macaque)[c('V1','V2', 'V3A', 'V4')]
E(macaque)[c('V1|V2','V2|V3A','V3A|V4')]
E(macaque, path = c('V1', 'V2', 'V3A', 'V4'))

V(macaque)['V1','V2',nei('V1'), nei('V2')] %>% 
  induced_subgraph(graph = macaque) %>%
  summary()

#V(macaque)['V1','V2',neighbors('V1'), neighbors('V2')] %>% 
#  induced_subgraph(graph = macaque) %>%
#  summary()  ## not working

is_connected(macaque, mode = "weak") #if it's directed graph,it has all edges connected if it's undirected graph
is_connected(macaque, mode = "strong")

V(macaque)[degree(macaque) < 2]
V(macaque)[innei('V1')]
V(macaque)[outnei('V1')]
V(macaque)[inc('V1|V2')] # select vertices that are incident to a given edge

data(kite)
kite %>% ends('A|D')
c(V(kite)['A'], V(kite)['D'])
V(kite)
rev(V(kite))
unique(V(kite)['A','A'])

union(V(kite)[1:5], V(kite)[6:10])
intersection(V(kite)[1:7], V(kite)[5:10])
difference(V(kite), V(kite)[1:5])

sub_macaque <- induced_subgraph(macaque, c('V1','V2','V4','MT'))
c(V(macaque)[11:20] %>% as_ids(), V(sub_macaque) %>% as_ids())

E(kite)
E(kite, path = c('A','D','C'))
E(kite)['A' %--% 'B']
E(kite)['A' %->% 'B']
E(kite)[1:3, 7:10]
E(kite)[seq_len(gsize(kite)) %% 2]
E(kite)[inc('D')]
E(macaque)[from('V1')]
E(macaque)[to('V1')]
E(kite)['A|B', 'B|C', 'D|A']

C(E(kite)['A|B'], E(kite)['D|A'])
rev(E(kite))
unique(E(kite)[1:5,1:10])

union(E(kite)[1:5], E(kite)[6:10])

kite['A','B']
d <- c('A','B','C','D')
kite[d,d] # Adjacency matrix

kite['A',]
kite[]
kite[1,-1]
degree(kite)
kite[degree(kite)>=4, degree(kite)<4]
kite[from = c('A','B','C'), to = c('C','D','E')]
macaque['V2', 'PIP'] # 1
macaque['PIP','V2'] # 0

neighbors(kite, "A")
kite[["A"]]
kite["A"]
kite['A','B']
kite[c('A','B')]
kite[[c('A','B')]]
macaque[['V2',]] # successors
macaque[[,'V2']] # predecessor
macaque %>% neighbors('V2')

#incident edge
kite[['A', edges = TRUE]]

data(UKfaculty)
V(UKfaculty)$Group

# make graph from scratch
kite <- make_empty_graph(directed = FALSE)+
  vertices(LETTERS[1:10])+
  edges('A','B', 'A','C', 'A','D', 'A','F',
        'B','D', 'B','E', 'B','G',
        'C','D', 'C','F',
        'D','E', 'D','F', 'D','G',
        'E','G',
        'F','G', 'F','H',
        'G','H',
        'H','I',
        'I','J')
# predefined structures
make_directed_graph()
make_undirected_graph()
make_empty_graph()
make_full_graph()
make_full_bipartite_graph()
make_graph("Pertersen")
make_ring()
make_lattice()
make_star()
make_tree()
#convert a graph to igraph
graph_from_adjacency_matrix()
graph_from_edgelist()
graph_from_data_frame()
graph_from_incidence_matrix()
graph_from_graphnel()
graph_from_literal()
#sample from random graph model
sample_gnp() # Bernoulli graph
sample_gnm() # Erdos-Renyi random graph
sample_degseq() # random with given degree sequence
sample_grg() # geometric
sample_pa() # preferential attachment model
sample_sbm() # stochastic block-model
sample_smallworld() # small-world graph
sample_hrg() # hierachical random graph
sample_bipartite() # bipartite random graph

#from graph files
read_graph() # .GraphMl, .GML, .Pajek


rbind(as.vector(V(kite)), V(kite)$name)
kite['F','I'] <- 1
kite

star <- make_empty_graph(10)
star[]
star[-1,1] <- 1 # [-1,1] is last row first column of imaginary adj matrix
star

adjletters <- strsplit("adjacencymatrix","")[[1]]
adj <- make_empty_graph()
adj <- adj + unique(adjletters)
V(adj)
adj[from=adjletters[-length(adjletters)], to = adjletters[-1]]<- 1
adj
# delete edge
kite['F','I'] <- 0
kite

### Chapter 2
data("USairports")
summary(USairports)

sum(which_loop(USairports))
#53 self-loops that shouldn't have

USairports <- simplify(USairports, remove.loops= TRUE, remove.multiple = FALSE)
any(which_loop(USairports))
length(USairports[["BOS","JFK", edges = TRUE]][[1]])
# 14 from BOS to JFK
USairports[["BOS","JFK", edges = TRUE]][[1]][[1:5]]

air <- simplify(USairports, edge.attr.comb = list(Departures = "sum", Seats = 'sum',Passengers = 'sum', 'ignore'))
is_simple(air)

air[['BOS','JFK',edges=TRUE]][[1]][[1]]

flight <- V(air)['BDL','FLL','BOS','PBI']
E(air)$width <- 0
E(air,path = flight)$width <- 1
E(air)[[1]]

BDL_PBI <- E(USairports)['BDL'%->%'FLL', 'FLL'%->%'BOS', 'BOS'%->%'PBI']
BDL_PBI[[]]
BDL_PBI[Carrier =='JetBlue Airways'][[]]

## shortest paths
distances(air, c('BOS','JFK','PBI','AZO'),c('BOS','JFK','PBI','AZO'))
shortest_paths(air, from='BOS',to='AZO')$vpath
all_shortest_paths(air, from='BOS',to='AZO')$res

## weighted graphs
wair <- simplify(USairports, edge.attr.comb = list(Departures='sum',Seats='sum',Passengers='sum',Distance='first','ignore'))
E(wair)$weight <- E(wair)$Distance
summary(wair)
distances(wair, c('BOS','JFK','PBI','AZO'), c('BOS','JFK','PBI','AZO'))
shortest_paths(wair, from='BOS', to='AZO')$vpath
all_shortest_paths(wair,from='BOS',to='AZO')$res
# unweighted it will use BFS
# weighted it will use Dijkstra's algorithm : visited set to unvisited nodes + BFS
# negative edge wt distances() uses Johnson's or Bellman-Ford, can't use shortest_paths()

#diameter is the largest distance of a graph
# real networks usually have a small diameter compared to their size (small world)
# diameter() will return largest non-isolated vertices if there are some isolated vertices

diameter(air)
dia_v <- get_diameter(air)
dia_e <- E(air, path=dia_v)
dia_v[[]]
dia_e[[]]

air_filt <- delete_edges(air,E(air)[Passengers<=10])
summary(air_filt)
summary(air)

diameter(air_filt)
diaf_v <- get_diameter(air_filt)
diaf_e <- E(air_filt, path = diaf_v)
diaf_v[[]]
diaf_e[[]]

mean_distance(air)
air_dist_hist <- distance_table(air)
air_dist_hist

barplot(air_dist_hist$res, names.arg = seq_along(air_dist_hist$res))


is_connected(air)
count_components(air)
components(air)$csize

bow_tie <- make_graph(~A-B-C-A-D-E-A)
biconnected_components(bow_tie)$components
articulation_points(bow_tie)

pc_comps <- decompose(air)
vapply(pc_comps, function(g) biconnected_components(g)$no)

## strongly connected components
is_connected(air, mode = 'weak')
is_connected(air, mode = 'strong')
count_components(air, mode = 'strong')
table(components(air,mode='strong')$membership)

## tree
tree3 <- make_tree(10, children = 3) %>% add_layout_(as_tree())
plot(tree3)

## minimum spanning trees
# weighted graph G, MST(G) is subset of G
# For example, US airport graph which contains only edges with most transported passengers
tree_air <- air
E(tree_air)$weight <- - E(tree_air)$Passengers
air_mst <- mst(tree_air)
plot(air_mst)

## DAGs
# tree is acyclic graph
# as same as DAGs is Directed acyclic graph
igraph_deps <- make_graph(~lattice -+ Matrix -+ igraph)
# lattice -> matrix -> igraph
is_dag(igraph_deps)
topo_sort(igraph_deps) # give a topological ordering of the graph
# Acyclic -> finding shortest longest paths easier
# used for scheduling and planning 

## Transitivity
# ego-network 
make_ego_graph(air, nodes=c('BOS','PBI'))%>% 
  lapply(summary) %>%
  invisible()

# k-neighborhood
# a vertex containing all vertices within k steps and all edges among them
# ego-network == k=1
air_deg <- degree(air)
air_ego_dens <- make_ego_graph(air) %>%
  vapply(edge_density, numeric(1))
airclusters0 <- data.frame(stringsAsFactors = FALSE, deg = air_deg, dens = air_ego_dens) %>%
  na.omit() %>%
  kmeans(centers = 4)
airclusters0$size
?edge_density

g <- graph(c(1,2, 2,3, 2,4, 3,4))
g <- simplify(g)
plot(g)
plot(make_ego_graph(g)[[1]],1)
plot(make_ego_graph(g)[[2]],1)
plot(make_ego_graph(g)[[3]],1)
plot(make_ego_graph(g)[[4]],1)
edge_density(g)
make_ego_graph(g) %>% vapply(edge_density, 1)

which(airclusters0$cluster==3)
air_deg[airclusters0$cluster==2] %>%
  summary()

air_deg[airclusters0$cluster==4] %>% 
  summary()

transitivity(air, vids = c('BOS','LAS'), type = 'local')
# transitivity is edge density without edges between ego and the alters (non-egos)
ego_size(air, nodes = c('BOS','LAS'))

transitivity(air, type = 'global')
# ratio of no. of triangles and no. of connected triples


### maximum flows and minimum cuts
E(air)[['BOS' %->% 'JFK']]
# source to sink vertex 
# every vertex in-flow = out-flow
# except source vertex (in-flow = 0)
# sink vertex (out-flow = 0)
# maximum flow is flow with largest value

## push-relabel algorithm by Goldberg and Tarjan
# label with height and water flow from higher to lower
E(air)$capacity <- E(air)$Seats
max_flow(air, 'BOS','PBI')$value
max_flow(air, 'BOS','LAX')$value
# min cut - mimimum number of edges that disconnect a destination v from a departure v
# weighted graph -> total capacity needed to disconnect
min_cut(air, 'BOS','LAX') # capacity
min_cut(air, 'BOS','LAX', capacity = rep(1, gsize(air)))
