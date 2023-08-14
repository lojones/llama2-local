# Run Llama 2 locally

[Instruction video on Youtube here](https://youtu.be/44etcb6Y_Z0)

This video describes the following:

1. **Download the Model:**
   - Download a large 7GB model.
   - Once downloaded, create a folder on your computer.
   - Copy the downloaded model into the newly created folder, which will be used as the working directory.

2. **Set Up the Python Environment:**
   - Set up a Python virtual environment for isolating project dependencies.
   - Activate the virtual environment.
   - Open VS Code from the working folder to let it recognize the virtual environment.
   - Use the `requirements.txt` file (a best practice in Python) to install dependencies.
   - Add the "Llama CPP Python" dependency to the `requirements.txt` file.
   - Install the added dependency using the `pip install` command.
   - Install a C++ compiler. Instructions vary depending on the OS; the video follows Windows instructions, installing Digital Studio Community which includes a C++ compiler.

3. **Interact with the Language Model:**
   - Open VS Code and create a new Python script named "ask_llama.py".
   - Import the Lamo CPP Python library.
   - Specify the path to the locally stored Llama model file in the script.
   - For testing, ask the model a simple question, e.g., "What are the names of the days of the week?"
   - Pass the question to the Llama model and write the output so it can be viewed.
   - Note: Executing this can be resource-intensive, consuming CPU and memory.
   - Run the script interactively in VS Code to step through each line of the code.
   - Set a breakpoint and click "run" to begin execution.
   - Monitor the CPU and memory usage during the model's processing.
   - Once the model finishes processing, it displays the answer to the question.
