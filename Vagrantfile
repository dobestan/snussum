# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.hostname = "dev.snussum.com"
  config.vm.network "private_network", ip: "192.168.57.36"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "deploy/vagrant.yml"
  end
end
