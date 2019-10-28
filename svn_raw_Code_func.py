import pysvn
client = pysvn.Client()

# <----------- Checking out a working copy --------->
client.checkout('http://url/example/path','./Dir/toCheckout')



# <----------- Update working copy --------->
client.update('./pathToDir/pysvn')

# <----------- Commit changes to the repository --------->
# edit the file foo.txt
f = open('./examples/pysvn/foo.txt', 'w')
f.write('Sample versioned file via python\n')
f.close()
# checkin the change with a log message
client.checkin(['./examples/pysvn'], 'Corrected spelling of python in foo.txt')

# <----------- Remove a file (or) directory from the working copy --------->
#  the file will be removed from the working copy
client.remove('./examples/pysvn/file.txt')
#committing the change removes the file from the repository
client.checkin(['./examples/pysvn/file2.txt'], 'Removing sample file')