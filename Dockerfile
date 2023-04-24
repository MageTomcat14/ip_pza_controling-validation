FROM ubuntu:20.04

# Install Packages
RUN apt-get update && DEBIAN_FRONTEND=noninteractive TZ=Europe/Paris \
    apt-get -y install \
        python3 python3-pip \
        git

# Append udev and libusb for device autodetection
RUN apt-get -y install udev
RUN apt-get -y install libusb-1.0-0

# Pip installations
RUN pip install robotframework
RUN pip install robotframework-seleniumlibrary
RUN pip install -e "git+https://github.com/Panduza/panduza-py.git@main#egg=panduza&subdirectory=client"