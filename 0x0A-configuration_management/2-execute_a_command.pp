# Manifest that kills a process named killmenow.

exec { 'killmenow_process':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
