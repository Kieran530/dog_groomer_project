// document.addEventListener("DOMContentLoaded", function () {
//     const buttonData = {
//         "trim-button": {
//             disableButtons: ["haircut-button", "specialty-cut-button"],
//         },
//         "haircut-button": {
//             disableButtons: ["trim-button", "specialty-cut-button"],
//         },
//         "specialty-cut-button": {
//             disableButtons: ["trim-button", "haircut-button"],
//         },
//         "basic-wash-button": {
//             disableButtons: ["premium-wash-button"],
//         },
//         "premium-wash-button": {
//             disableButtons: ["basic-wash-button"],
//         },
//     };

//     const allBtns = document.querySelectorAll("#services-container button");
//     for (const button of allBtns) {

//         button.addEventListener("click", () => {
//             const buttonId = button.id;
//             if (buttonData.hasOwnProperty(buttonId)) {
//                 const disableButtons = buttonData[buttonId].disableButtons.map(
//                     (btn) => document.getElementById(btn)
//                 );
//                 toggleButtons(disableButtons);
//             }
//             button.classList.toggle("active");
//         });
//     }

//     function toggleButtons(buttons) {
//         buttons.forEach(
//             (button) => (button.disabled = !button.disabled) // Toggle disabled state
//         );
//         console.log("hey its working!");
//     }
// });

// console.log("DOM content loaded"); // Check if this message appears in the console


// function updateSelectedOptions() {
//     const selectedButtons = document.querySelectorAll(".service_buttons button.active");
//     const selectedOptions = Array.from(selectedButtons).map(button => button.innerText.trim());
//     document.getElementById("selectedOptions").value = JSON.stringify(selectedOptions);
// }



// document.addEventListener("DOMContentLoaded", function () {
//     const checkboxData = {
//         "trim-button": {
//             disableCheckboxes: ["haircut-button", "specialty-cut-button"],
//         },
//         "haircut-button": {
//             disableCheckboxes: ["trim-button", "specialty-cut-button"],
//         },
//         "specialty-cut-button": {
//             disableCheckboxes: ["trim-button", "haircut-button"],
//         },
//         "basic-wash-button": {
//             disableCheckboxes: ["premium-wash-button"],
//         },
//         "premium-wash-button": {
//             disableCheckboxes: ["basic-wash-button"],
//         },
//     };

//     const allCheckboxes = document.querySelectorAll("#services-container input[type='checkbox']");
//     for (const checkbox of allCheckboxes) {
//         checkbox.addEventListener("change", () => {
//             const checkboxId = checkbox.id;
//             if (checkboxData.hasOwnProperty(checkboxId)) {
//                 const disableCheckboxes = checkboxData[checkboxId].disableCheckboxes.map(
//                     (cb) => document.getElementById(cb)
//                 );
//                 toggleCheckboxes(disableCheckboxes, checkbox.checked);
//             }
//         });
//     }

//     function toggleCheckboxes(checkboxes, enabled) {
//         checkboxes.forEach((checkbox) => {
//             checkbox.disabled = !enabled;
//             checkbox.parentNode.classList.toggle("disabled", !enabled);
//         });
//     }
// // });
$(document).ready(function() {
    $('#1-checkbox').on('change', function() {
      if ($(this).prop('checked')) {
        $('#2-checkbox').prop({ disabled: true, checked: false });
      } else {
        $('#2-checkbox').prop('disabled', false);
      }
    });
  
    $('#2-checkbox').on('change', function() {
      if ($(this).prop('checked')) {
        $('#1-checkbox').prop({ disabled: true, checked: false });
      } else {
        $('#1-checkbox').prop('disabled', false);
      }
    });
  
    $('#3-checkbox').on('change', function() {
      if ($(this).prop('checked')) {
        $('#4-checkbox, #5-checkbox').prop({ disabled: true, checked: false });
      } else {
        $('#4-checkbox, #5-checkbox').prop('disabled', false);
      }
    });
  
    $('#4-checkbox').on('change', function() {
        if ($(this).prop('checked')) {
          $('#3-checkbox, #5-checkbox').prop({ disabled: true, checked: false });
        } else {
          $('#3-checkbox, #5-checkbox').prop('disabled', false);
        }
      });

      $('#5-checkbox').on('change', function() {
        if ($(this).prop('checked')) {
          $('#4-checkbox, #3-checkbox').prop({ disabled: true, checked: false });
        } else {
          $('#4-checkbox, #3-checkbox').prop('disabled', false);
        }
      });

});