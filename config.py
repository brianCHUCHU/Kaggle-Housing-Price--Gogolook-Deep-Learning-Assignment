import os
import errno
import requests

FOLDERS = {
    'housing-prices': ['data','data','data','data']
}
FILENAMES = {
    'housing-prices': ['train.csv','test.csv','data_description.txt','sample_submission.csv']
}

def download(folderName, branch='master'):
    base_url = 'https://raw.githubusercontent.com/joccing/ICT303-assignment1/{}/'.format(branch)

    folders = FOLDERS[folderName]
    filenames = FILENAMES[folderName]
    for folder, filename in zip(folders, filenames):
        if len(folder):
            try:
                os.mkdir(folder)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        if len(filename):
            path = os.path.join(folder, filename)
            url = '{}{}'.format(base_url, path)
            r = requests.get(url, allow_redirects=True)
            open(path, 'wb').write(r.content)
    
def config_data(branch='master'):
        print('Downloading files from GitHub repo ...')
        download('housing-prices', branch)
        print('Finished!')