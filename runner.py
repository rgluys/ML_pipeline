from logger_config import setup_logger
from MyDataScienceFlow import MyDataScienceFlow
from metaflow import Flow


if __name__ == '__main__':
    # Configure logger
    setup_logger('pipeline.log')

    # Start the Metaflow flow
    with Flow(MyDataScienceFlow) as flow:
        # Run the flow
        flow.run()
