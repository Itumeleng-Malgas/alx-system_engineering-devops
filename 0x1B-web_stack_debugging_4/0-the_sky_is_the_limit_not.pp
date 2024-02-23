#  Sky is the limit, let's bring that limit higher

# Increase ULIMIT
exec { 'increase-limit':
    command => "/bin/sed -i 's/15/4096/' /etc/default/nginx",
    path    => "/usr/local/bin/:/bin/",
}

# Restart nginx
exec { 'restart-nginx':
    command => "/etc/init.d/nginx restart",
    path    => "/etc/init.d",
}
