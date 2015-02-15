# -*- mode: ruby -*-

Vagrant.configure(2) do |config|
  config.vm.provider "parallels" do |v|
    v.check_guest_tools = false
    v.memory = 512
    v.cpus = 1
  end

  config.vm.box = "parallels/ubuntu-14.04"
  config.vm.box_check_update = false
  config.vm.network "private_network", type: "dhcp"

  config.vm.define "redis" do |redis|
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "redis.yml"
    ansible.sudo = true
    ansible.extra_vars = {
      ansible_ssh_user: "vagrant"
    }
  end

end
