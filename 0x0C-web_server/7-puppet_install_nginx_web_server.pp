# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Define the default site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "server {
    listen 80;
    server_name localhost;

    location / {
        echo 'Hello World!';
    }

    location /redirect_me {
        return 301 https://example.com/;
    }
}\n",
  notify  => Service['nginx'],
}

# Reload Nginx after making changes
exec { 'reload_nginx':
  command     => '/bin/kill -s HUP $(cat /var/run/nginx.pid)',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
