#!/usr/bin/env bash
# using puppet

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"
	#ssh config
	host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
