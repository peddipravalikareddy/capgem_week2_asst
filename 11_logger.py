#11
#Create a class `Logger` with a method `log(message)`. 
# Implement method overloading to log different message types (`error`, `warning`, `info`).

class Logger:
    def log(self, error=None, warning=None, info=None):
        self.error = error
        self.warning = warning
        self.info = info
        if error and warning and info:
            print(f"Error message: {error}\nWarning message: {warning}!\nInformation message: {info}")
        elif error and warning:
            print(f"Error message: {error}\nWarning message: {warning}!")
        elif error and info:
            print(f"Error message: {error}\nInformation message: {info}")
        elif error:
            print(f"Error message: {error}")
        elif warning and info:
            print(f"Warning message: {warning}!\nInformation message: {info}")
        elif warning:
            print(f"Warning message: {warning}!")
        else:
            print(f"Information message: {error}")
obj = Logger()
