import argparse

parser = argparse.ArgumentParser(description="Train a model")
parser.add_argument("--epochs", type=int, default=10, help="Number of epochs")
parser.add_argument("--lr", type=float, default=0.001, help="Learning rate")

args = parser.parse_args()

print(f"Training for {args.epochs} epochs with LR = {args.lr}")
