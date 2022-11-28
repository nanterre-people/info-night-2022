resource "outscale_vm" "my_vm" {
  image_id                 = var.image_id
  vm_type                  = var.vm_type
  keypair_name             = outscale_keypair.my_keypair.keypair_name
  security_group_ids       = [outscale_security_group.my_sg.security_group_id]
  placement_subregion_name = "${var.region}a"
  placement_tenancy        = "default"

  tags {
    key   = "osc.fcu.eip.auto-attach"
    value = outscale_public_ip.my_public_ip.public_ip
  }

  provisioner "file" {
    source      = "vm_startup.sh"
    destination = "/tmp/vm_startup.sh"
    connection {
      type        = "ssh"
      user        = "outscale"
      host        = self.public_ip
      private_key = tls_private_key.my_key.private_key_pem
    }
  }

  provisioner "remote-exec" {
    inline = [
      "sudo bash /tmp/vm_startup.sh"
    ]
    connection {
      type        = "ssh"
      user        = "outscale"
      host        = self.public_ip
      private_key = tls_private_key.my_key.private_key_pem
    }
  }
}
