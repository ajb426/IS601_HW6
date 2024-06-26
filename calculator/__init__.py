import os
import logging
import logging.config
from dotenv import load_dotenv
from calculator.plugin_manager import PluginManager
from calculator.command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, GetHistoryCommand, ClearHistoryCommand, GetLastCalculationCommand


class CalculatorApp:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.commands = self.initialize_default_commands()
        self.plugin_manager = PluginManager(self.commands)
        self.load_plugins()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings
    
    def initialize_default_commands(self):
        commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand(),
            'history': GetHistoryCommand(),
            'clear_history': ClearHistoryCommand(),
            'last': GetLastCalculationCommand()
        }
        logging.info("Default commands initialized: %s", list(commands.keys()))
        return commands

    def load_plugins(self):
        self.plugin_manager.load_plugins()

    def start_repl(self):
        from calculator.repl import CalculatorREPL
        repl = CalculatorREPL(self.commands)
        repl.start()

    def start(self):
        logging.info("Application started. Type 'exit' to exit.")
        self.start_repl()

if __name__ == "__main__":
    app = CalculatorApp()
    app.start()
