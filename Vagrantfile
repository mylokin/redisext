# -*- mode: ruby -*-

Vagrant.configure(2) do |config|
  config.vm.provider "parallels" do |v|
    v.check_guest_tools = false
    v.memory = 512
    v.cpus = 1
  end

  config.vm.define "redis" do |redis|
    redis.vm.box = "parallels/ubuntu-14.04"
    redis.vm.box_check_update = false
    redis.vm.network "private_network", type: "dhcp"
    redis.vm.network :forwarded_port, host: 6379, guest: 6379
    redis.vm.provision "ansible" do |ansible|
      ansible.playbook = "redis.yml"
      ansible.sudo = true
      ansible.extra_vars = {
        ansible_ssh_user: "vagrant"
      }
    end
  end
end
