library(igraph)
library(readr)
library(tidyverse)

## set current folder path and language
readpath <- function(){
  return(readline("Enter your folder path: "))
}
setwd(readpath())
Sys.setlocale('LC_CTYPE','Thai')
options(encoding = 'UTF-8')

## read full edge and full vertex files
edge <- read_csv('fulledge.csv')
edge <- edge[,2:4]
vertex <- read_csv('fullvertex.csv')
vertex <- vertex[,2:3]

## use fulledge graph 
fulledge <- edge
g2 <- graph_from_data_frame(fulledge, directed = TRUE)
c<- components(g2)
fullvertex <- names(c$membership[c$membership==1])
g2.sub <- induced_subgraph(g2, fullvertex)
diameter(g2.sub)
d <- degree(g2.sub)
tb <- table(d)
plot(x = as.integer(rownames(tb)), y = tb)
plot(x = log(as.integer(rownames(tb))), y = log(tb))# power law
radius(g2.sub) # 7
average.path.length(g2.sub, directed = FALSE) #4.594

## use only edge that have vertices in fullvertex
sum(sapply(edge$to, function(x) !(x %in% vertex$name)))
edge <- edge[sapply(edge$to, function(x) (x %in% vertex$name)),]
g <- graph_from_data_frame(edge,directed=TRUE,vertices = vertex)
diameter(g)
diameter(g,directed = FALSE)
d <- degree(g)
tb <- table(d)
plot(x = as.integer(rownames(tb)), y = tb)

# delete unconnected vertex
c <- components(g)
vertices <- names(c$membership[c$membership==1])
g.sub <- induced_subgraph(g, vertices)
diameter(g.sub)
diameter(g.sub, directed = FALSE)
d <- degree(g.sub)
tb <- table(d)
plot(x = as.integer(rownames(tb)), y = tb)
plot(x = log(as.integer(rownames(tb))), y = log(tb))
g.undi <- as.undirected(g.sub, mode = 'collapse')
average.path.length(g.sub, directed = FALSE) # 4.3077
radius(g.undi) # 7 

## export graph to .graphml
#write_graph(g.sub, 'wikigraphfull.graphml', format= 'graphml')
#write_graph(g2.sub, 'wikigraphfulledge.graphml', format= 'graphml')
