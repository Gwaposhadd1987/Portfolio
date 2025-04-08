import '../css/main.css'
import 'flowbite';
import htmx from 'htmx.org';
import Alpine from 'alpinejs';

// Make AlpineJS globally accessible
window.Alpine = Alpine

Alpine.start()
// Make HTMX globally accessible
window.htmx = htmx