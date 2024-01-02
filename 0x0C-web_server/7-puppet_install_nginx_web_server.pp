# Install Nginx web server (w/ Puppet) 

$nginx_version = 'installed'
$nginx_site_path = '/etc/nginx/sites-enabled/default'
$nginx_html_path = '/var/www/html/index.html'
$nginx_html_content = 'Hello World!'
$nginx_service_name = 'nginx'

package { 'nginx':
  ensure => $nginx_version,
}

file_line { 'configure_nginx_redirect':
  ensure => 'present',
  path   => $nginx_site_path,
  after  => 'listen 80 default_server;',
  line   => 'location /redirect_me { return 301 https://notreachable.com/; }',
}

file { $nginx_html_path:
  content => $nginx_html_content,
}

service { $nginx_service_name:
  ensure  => 'running',
  require => Package['nginx'],
}
