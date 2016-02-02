# idneo


## Prerequisites
+ [Git](http://git-scm.com/)
+ [Oracle's VirtualBox](https://www.virtualbox.org/)
+ [Vagrant](http://www.vagrantup.com/)
+ [Python](http://www.python.org/)
+ [Fabric](http://www.fabfile.org/)


## Configuring your virtual environment
1. Fork the repo with your Github's user

2. Clone your fork

    ```bash
    $ git clone --recursive git@github.com:{ your username }/idneo.git
    ```

3. Create the virtual machine

    ```bash
    $ cd idneo
    $ vagrant up
    ```

4. Build the environment inside the virtual machine

    ```bash
    $ fab environment:vagrant bootstrap
    ```

5. Run the development server

    ```
    $ fab environment:vagrant runserver
    ```

6. Open your web browser and check the project at `127.0.0.1:8000`


## Useful fabric commands

### resetdb
Drop and rebuild a fresh database instance for the project.
```bash
$ fab environment:vagrant resetdb
```

### pip_install \[upgrade=boolean\]
Install the Python dependencies for the project specified in the proper requirements file for the given environment.
```bash
# Installing dependencies
$ fab environment:vagrant pip_install

# Install and upgrading dependencies
$fab environment:vagrant pip_install:upgrade=True
```

### runserver
Run the development server inside the virtual machine.
```bash
$ fab environment:vagrant runserver
```