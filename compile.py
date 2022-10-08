import os


def compileFile(to, fileName):
    with open(f'src/{fileName}.css', 'r') as file:
        name = '' if fileName == 'base' else fileName
        ident = 'url-prefix' if fileName == 'base' else 'url'
        to.write(f'\n@-moz-document {ident}("https://www.last.fm/{name}")')
        to.write('\n{\n')
        for line in file:
            to.write(line)
        to.write('\n}\n')


def export():
    with open('lastfm-5am.css', 'w+') as exportFile:
        exportFile.truncate()
        for file in os.listdir('./src'):
            compileFile(exportFile, file.replace('.css', ''))


if __name__ == '__main__':
    export()
