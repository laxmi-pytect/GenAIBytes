# GenAIBytes
A collection of examples to leverage Gen AI models

This repo contains example implementation of Gen AI concepts, simplified in a very basic unit as Bytes, and building forwards.

##Geminiapiplayground - This shows how you can view what models are present in Gemini currently

##BuildingEmbeddings- When talking about RAG (Retrival Argument Model), basic entity is Embeddings. This notebook exercise shows how to build basic embedding, how to store  and how to query them.

##Langchains-basic chat models and prompts- This notebooks demonstrates the examples how langchain basic chat model can be used, also it's limitations.

###Streamlit_Multimodal_apis: This exercise demonstrate how multimodal apis (text to image, image to text, video to text etc) can be leveraged with streamlit(platform for UI interface in fractions) to build quick features.

###ModelcontextProtocol(MCP): This exercise demonstate simple use case of client server interaction with MCP over transport protocol-stdio.
Client - leverage MCP and Gemini LLM'. Using MCP, it establishes connection with MCP server, loads the tools from server; with Langchain and Gemini creates a react (reasoning and acting) agent and invokes the agent for tools to fetch the result of query.
Server- leverages MCP and deploys the tool.

TBC
