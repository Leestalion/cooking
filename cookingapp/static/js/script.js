const ID_RE = /(-)_(-)/;


/**
 * Replace the template index of an element (-_-) with the
 * given index.
 */
function replaceTemplateIndex(value, index) {
    return value.replace(ID_RE, '$1'+index+'$2');
}


/**
 * Adjust the indices of form fields when removing items.
 */

function adjustindices(removedIndex, type) {
    if (type == "step") {
        var $forms = $('.subform_step');
    } else {
        var $forms = $('.subform_ing');
    }

    $forms.each(function(i) {
        var $form = $(this);
        var index = parseInt($form.data('index'));
        var newIndex = index-1;

        if (index < removedIndex) {
            // Skip
            return true;
        }

        // This will replace the original index with the new one
        // only if it is found in the format -num-, preventing
        // accidental replacing of fields that may have numbers
        // intheir names.
        var regex = new RegExp('(-)'+index+'(-)');
        var repVal = '$1'+newIndex+'$2';

        // Change ID in form itself
        $form.attr('id', $form.attr('id').replace(index, newIndex));
        $form.data('index', newIndex);

        // Change IDs in form fields

        if (type == "step") {
            var balises = 'label, textarea';
        } else {
            var balises = 'label, input, select'
        }

        $form.find(balises).each(function(j) {
            var $item = $(this);

            if ($item.is('label')) {
                // Update labels
                $item.attr('for', $item.attr('for').replace(regex, repVal));
                return;
            }

            // Update other fields
            if($item.attr('id') && $item.attr('name')) {
                $item.attr('id', $item.attr('id').replace(regex, repVal));
                $item.attr('name', $item.attr('name').replace(regex, repVal));
            }
            })
    })
}

/**
 * Remove a form.
 */
function removeForm(event) {
    var type = event.data.type

    if (type == "step") {
        var $removedForm = $(this).closest('.subform_step');
    } else {
        var $removedForm = $(this).closest('.subform_ing');
    }

    var removedIndex = parseInt($removedForm.data('index'));

    $removedForm.remove();

    // Update indices
    adjustindices(removedIndex, type);
}

/**
 * Add a form.
 */
function addForm(event) {
    var type = event.data.type
    if (type == "step") {
        var $templateForm = $('#step-_-form');
    } else {
        var $templateForm = $('#ingredient-_-form');
    }

    if ($templateForm.length === 0) {
        console.log('[ERROR] Cannot find template');
        return;
    }

    // Get Last index

    if (type == "step") {
        var $lastForm = $('.subform_step').last();
    } else {
        var $lastForm = $('.subform_ing').last();
    }
    var newIndex = 0;

    if ($lastForm.length > 0) {
        newIndex = parseInt($lastForm.data('index')) + 1;
    }

    // Maximum of 20 subforms
    if (newIndex >= 20) {
        console.log('[WARNING] Reached maximum number of elements');
        return;
    }

    // Add elements
    var $newForm = $templateForm.clone();

    $newForm.attr('id', replaceTemplateIndex($newForm.attr('id'), newIndex));
    $newForm.data('index', newIndex);

    if (type == "step") {
        var balises = 'label, textarea';
    } else {
        var balises = 'label, input, select'
    }

    $newForm.find(balises).each(function(idx) {
        var $item = $(this);
        if ($item.is('label')) {
            // Update labels
            $item.attr('for', replaceTemplateIndex($item.attr('for'), newIndex));
            return;
        }

        // Update other fields
        if($item.attr('id') && $item.attr('name')) {
            $item.attr('id', replaceTemplateIndex($item.attr('id'), newIndex));
            $item.attr('name', replaceTemplateIndex($item.attr('name'), newIndex));
        }
        
    });

    // Append
    if (type == "step") {
        $('#step_subforms_container').append($newForm);
        $newForm.addClass('subform_step');
    } else {
        $('#ingredient_subforms_container').append($newForm);
        $newForm.addClass('subform_ing');

        $newForm.find('select').formSelect();
    }

    $newForm.removeClass('is-hidden');

    if (type == "step") {
        $newForm.find('.removeStep').click({type: "step"}, removeForm);
    } else {
        $newForm.find('.removeIngredient').click({type: "ingredient"}, removeForm);
    }
}



$(document).ready(function() {
    $('#ingredient-0-form').find("select").formSelect();
    $('.modal').modal();
    $('.select-force-update').formSelect();
    $('.sidenav').sidenav();

    $('#addStep').click({type: "step"}, addForm);
    $('#addIngredient').click({type: "ingredient"}, addForm)
    $('.removeStep').click({type: "step"}, removeForm);
    $('.removeIngredient').click({type: "ingredient"}, removeForm);
})