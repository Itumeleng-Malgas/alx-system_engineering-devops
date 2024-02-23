#  Sky is the limit, let's bring that limit higher

# Increase ULIMIT
exec {
    command => "/bin/sed -i 's/15/4096/' /etc/default/nginx",
    path    => "/usr/local/bin/:/bin/",
}

# Restart nginx
exec {
    command => "/etc/init.d/nginx restart",
    path    => "/etc/init.d",
}
