from charms.reactive import render_template, hooks
from charmhelpers.core.hookenv import log, config, status_set
from charmhelpers.fetch import apt_install, filter_installed_packages


def install_packages():
    # for storing the packages to be installed
    packages = ['etckeeper']

    log("Determining DVCS packages")
    dvcs = config['dvcs']
    packages.append(dvcs)
    filtered_packages = filter_installed_packages(packages)

    log("Ensuring etckeeper and DVCS is installed")
    apt_install(filtered_packages)

    filtered_packages = filter_installed_packages(packages)
    log("Checking if packages were installed")
    if (len(filtered_packages) > 0):
        log("Failed to install packages {}".format(filtered_packages))
        status_set("error", "Package installation failed")
    else:
        log("Packages successfully installed")
        status_set("active", "etckeeper installed")


@hooks.hook('install.real')
def install_hook():

    log("Installing packages during install hook")
    status_set("maintenance", "Installing packages")

    install_packages()


@hooks.hook('config.changed')
def configure_etckeeper():
    log("Checking packages and configuration")
    status_set("maintenance", "Installing packages and configuring etckeeper")

    install_packages()

    log("Configuring etckeeper")
    render_template('etckeeper.conf.jinja', '/etc/etckeeper.conf')
