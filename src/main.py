import click
import yaml
from dataset_dataloader import dataset_dataloader
from model import training
from test import test

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config
@click.command()
@click.option('--config-path', default='../config.yaml', help='Path to the .yaml file')
def main(config_path):
    config = load_config(config_path)
    data_root = config['paths']['data']
    train_loader, test_loader,val_loader=dataset_dataloader.dataset_dataloader(data_root)
    model,device=training.train(train_loader, test_loader,val_loader)
    test.test(test_loader,model,device)


if __name__ == "__main__":
    main()