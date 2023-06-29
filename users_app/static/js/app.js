
$(document).ready(function() {
    $('#1-checkbox').on('change', function() {
      if ($(this).prop('checked')) {
        // Disable the other checkbox
        $('#2-checkbox').prop({ disabled: true, checked: false });
        // Change the background color of the parent label
        $('#2-checkbox').parent('label').addClass('disabled')
      } else {
        $('#2-checkbox').prop('disabled', false);
        $('#2-checkbox').parent('label').removeClass('disabled')
      }
    });
  
    $('#2-checkbox').on('change', function() {
      if ($(this).prop('checked')) {
        $('#1-checkbox').prop({ disabled: true, checked: false });
        $('#1-checkbox').parent('label').addClass('disabled')
      } else {
        $('#1-checkbox').prop('disabled', false);
        $('#1-checkbox').parent('label').removeClass('disabled')
      }
    });
  
    $('#3-checkbox').on('change', function() {
      if ($(this).prop('checked')) {
        $('#4-checkbox, #5-checkbox').prop({ disabled: true, checked: false });
        $('#4-checkbox, #5-checkbox').parent('label').addClass('disabled')
      } else {
        $('#4-checkbox, #5-checkbox').prop('disabled', false);
        $('#4-checkbox, #5-checkbox').parent('label').removeClass('disabled')
      }
    });
  
    $('#4-checkbox').on('change', function() {
        if ($(this).prop('checked')) {
          $('#3-checkbox, #5-checkbox').prop({ disabled: true, checked: false });
          $('#3-checkbox, #5-checkbox').parent('label').addClass('disabled')
        } else {
          $('#3-checkbox, #5-checkbox').prop('disabled', false);
          $('#3-checkbox, #5-checkbox').parent('label').removeClass('disabled')
        }
      });

      $('#5-checkbox').on('change', function() {
        if ($(this).prop('checked')) {
          $('#4-checkbox, #3-checkbox').prop({ disabled: true, checked: false });
          $('#4-checkbox, #3-checkbox').parent('label').addClass('disabled')
        } else {
          $('#4-checkbox, #3-checkbox').prop('disabled', false);
          $('#4-checkbox, #3-checkbox').parent('label').removeClass('disabled')
        }
      });

});

$(document).ready(function() {
  // Calculate and update the total price
  function calculateTotalPrice() {
    var totalPrice = 0;
    $('.checkbox-input:checked').each(function() {
      console.log('this is reallllly working!')
      var priceElement = $(this).closest('.service_buttons').find('.price');
      console.log(priceElement)
      var price = parseFloat(priceElement.text().replace('$', ''));
      totalPrice += price;
      
    });
    $('#total-price').text(totalPrice.toFixed(2));
  }
  console.log('this is working!!')
  // Event listener for checkbox click
  $('.checkbox-input').on('change', function() {
    console.log('Checkbox changed');
    calculateTotalPrice();
  });

  // Initial calculation of total price
  calculateTotalPrice();
  function applySelectedClass() {
    $('.checkbox-input:checked').each(function() {
      $(this).parent('label').addClass('selected');
    });
  }
  
  function removeSelectedClass() {
    $('.checkbox-input').each(function() {
      if (!$(this).prop('checked')) {
        $(this).parent('label').removeClass('selected');
      }
    });
  }

  $('.checkbox-input').on('change', function() {
    console.log('Checkbox changed');
    calculateTotalPrice();
    applySelectedClass();
    removeSelectedClass();
  });


});