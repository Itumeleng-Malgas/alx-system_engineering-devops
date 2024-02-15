# fix wp-settings.phpp file extention.

exec { 'fix-bad-extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
