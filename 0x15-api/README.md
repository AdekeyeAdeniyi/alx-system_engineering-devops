Background Context
------------------

[![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/897638f42eb1bad6605d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221018T132306Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a1df1cf742caa5fe24bcdacf953f91f57fe08bb4bd2ec577e3cfcd94a6d17033)](https://youtu.be/-2kyU6-j8ZQ)

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

Resources
---------

**Read or watch**:

*   [Friends don’t let friends program in shell script](/rltoken/KMFzqRAqedMf7AHHBD_43g "Friends don't let friends program in shell script")
*   [What is an API](/rltoken/zeBO6_RNTlwaotyRRNAzoQ "What is an API")
*   [What is an API? In English, please](/rltoken/bf09Qp6QY44CANLzxxRbPA "What is an API? In English, please")
*   [What is a REST API](/rltoken/fA164QWEnZxaSngBD3EPRQ "What is a REST API")
*   [What are microservices](/rltoken/lktnmAVnhFFsg5zK2CXEKg "What are microservices")
*   [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](/rltoken/b7V1ROY6kSRxDDKnsJoqxg "PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/03Evn5VsICwJUAiTdu0zHA "explain to anyone"), **without the help of Google**:

### General

*   What Bash scripting should not be used for
*   What is an API
*   What is a REST API
*   What are microservices
*   What is the CSV format
*   What is the JSON format
*   Pythonic Package and module name style
*   Pythonic Class name style
*   Pythonic Variable name style
*   Pythonic Function name style
*   Pythonic Constant name style
*   Significance of CapWords or CamelCase in Python
