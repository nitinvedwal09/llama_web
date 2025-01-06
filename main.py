from langchain_ollama import OllamaLLM
model=OllamaLLM(model="llama3.1")
while True:
    prompt=input("input: ")
    prompt="""convert below text into hindi: Machine  Learning:  (i) Supervised  Learning:  regression  and classification  problems,  simple  linear  
    regression,  multiple  linear  regression,  ridge  regression,  logistic  regression,  k-nearest  neighbour,  
    naive  Bayes  classifier,  linear  discriminant  analysis,  support  vector  machine,  decision  trees,  bias-
    variance  trade -off, cross -validation  methods  such as leave -one-out (LOO)  cross -validation,  k-folds  
    cross -validation,  multi -layer  perceptron,  feed-forward  neural  network;  (ii) Unsupervised  Learning:  
    clustering  algorithms,  k-means/k -medoid,  hierarchical  clustering,  top-down,  bottom -up: single -
    linkage,  multiple -linkage,  dimensionality  reduction,  principal  component  analysis.  """
    result=model.invoke(input=prompt)
    print("response",result)