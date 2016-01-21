import click

@click.command()
@click.option('--printstatement', prompt='Put the thing to print here', help='What you type will be printed')
def main(printstatement):
	print(printstatement)

if __name__ == "__main__":
	main()