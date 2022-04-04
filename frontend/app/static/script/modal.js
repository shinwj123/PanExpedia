function openForm() {
    let inputVal = document.getElementById("email").value;
    alert(inputVal);
    
}
function closeForm() {
    document.getElementById("popupForm").style.display = "none";
}

function add() {
    let firstName = document.getElementById("userFirstName").value;
    let lastName = document.getElementById("userLastName").value;
    let destCity = document.getElementById("destinationCity").value;
    let email = document.getElementById("email").value;
    let pass = document.getElementById("password").value;
    alert(firstName);
    $.ajax({
        type: 'POST',
        url: '/create?first='+firstName+'&last='+lastName+'&destCity='+destCity+'&email='+email+'&pass='+pass,
        contentType: 'application/jason;charset=UTF-8',
        success: function (res) {
            console.log(res.response)
            location.reload();
        },
        error: function() {
            console.log('Error');
        }
    });
    console.log("Done with ajax");
};

function deleteOne() {
    let email = document.getElementById("deleteEmail").value;
    $.ajax({
        type: 'POST',
        url: '/delete?e='+email,
        contentType: 'application/jason;charset=UTF-8',
        success: function (res) {
            console.log(res.response);
            location.reload();
        },
        error: function() {
            console.log('Error');
        }
    });
};

function update() {
    let firstName = document.getElementById("userFirstNameUpdate").value;
    let lastName = document.getElementById("userLastNameUpdate").value;
    let destCity = document.getElementById("destinationCityUpdate").value;
    let email = document.getElementById("emailUpdate").value;
    let pass = document.getElementById("passwordUpdate").value;
    alert(firstName)
    $.ajax({
        type: 'POST',
        url: '/update?first='+firstName+'&last='+lastName+'&destCity='+destCity+'&email='+email+'&pass='+pass,
        contentType: 'application/jason;charset=UTF-8',
        success: function (res) {
            console.log(res.response);
            location.reload();
        },
        error: function() {
            console.log('Error');
        }
    });
};

function search() {
    let country = document.getElementById("searchCountry").value;
    $.ajax({
        type:'POST',
        url: '/search?c='+country,
        success: function (res) {
            console.log(res.response);
            location.reload();
        },
        error: function() {
            console.log('Error');
        }
    });
};

// $(document).ready(function () {
//     // example: https://getbootstrap.com/docs/4.2/components/modal/
//     // show modal
//     alert("HELLO");

    

//     // $('#task-modal').on('show.bs.modal', function (event) {
//     //     const button = $(event.relatedTarget) // Button that triggered the modal
//     //     const taskID = button.data('source') // Extract info from data-* attributes
//     //     const content = button.data('content') // Extract info from data-* attributes

//     //     const modal = $(this)
//     //     if (taskID === 'New Task') {
//     //         modal.find('.modal-title').text(taskID)
//     //         $('#task-form-display').removeAttr('taskID')
//     //     } else {
//     //         modal.find('.modal-title').text('Edit Task ' + taskID)
//     //         $('#task-form-display').attr('taskID', taskID)
//     //     }

//     //     if (content) {
//     //         modal.find('.form-control').val(content);
//     //     } else {
//     //         modal.find('.form-control').val('');
//     //     }
//     // })


//     // $('#submit-task').click(function () {
//     //     const tID = $('#task-form-display').attr('taskID');
//     //     console.log($('#task-modal').find('.form-control').val())
//     //     $.ajax({
//     //         type: 'POST',
//     //         url: tID ? '/edit/' + tID : '/create',
//     //         contentType: 'application/json;charset=UTF-8',
//     //         data: JSON.stringify({
//     //             'description': $('#task-modal').find('.form-control').val()
//     //         }),
//     //         success: function (res) {
//     //             console.log(res.response)
//     //             location.reload();
//     //         },
//     //         error: function () {
//     //             console.log('Error');
//     //         }
//     //     });
//     // });

//     // $('.remove').click(function () {
//     //     const remove = $(this)
//     //     $.ajax({
//     //         type: 'POST',
//     //         url: '/delete/' + remove.data('source'),
//     //         success: function (res) {
//     //             console.log(res.response)
//     //             location.reload();
//     //         },
//     //         error: function () {
//     //             console.log('Error');
//     //         }
//     //     });
//     // });

//     // $('.state').click(function () {
//     //     const state = $(this)
//     //     const tID = state.data('source')
//     //     const new_state
//     //     if (state.text() === "In Progress") {
//     //         new_state = "Complete"
//     //     } else if (state.text() === "Complete") {
//     //         new_state = "Todo"
//     //     } else if (state.text() === "Todo") {
//     //         new_state = "In Progress"
//     //     }

//     //     $.ajax({
//     //         type: 'POST',
//     //         url: '/edit/' + tID,
//     //         contentType: 'application/json;charset=UTF-8',
//     //         data: JSON.stringify({
//     //             'status': new_state
//     //         }),
//     //         success: function (res) {
//     //             console.log(res)
//     //             location.reload();
//     //         },
//     //         error: function () {
//     //             console.log('Error');
//     //         }
//     //     });
//     // });

// });