$(function () {
  $('#id_deadline').datetimepicker({
    format: 'YYYY-MM-DD',
    icons: {
      time: 'far fa-clock',
      date: 'far fa-calendar',
      up: 'fas fa-chevron-up',
      down: 'fas fa-chevron-down',
      previous: 'fas fa-chevron-left',
      next: 'fas fa-chevron-right',
      today: 'fas fa-calendar-check-o',
      clear: 'fas fa-trash',
      close: 'fas fa-times'
    }
  });
});
