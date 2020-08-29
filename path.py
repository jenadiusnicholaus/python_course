from pathlib import Path
path = Path('Ecommerce_parkage')
print(path.exists())


# search all exiting directories
for file in path.glob('*.py'):
    print(file)
