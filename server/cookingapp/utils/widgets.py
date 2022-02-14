from markupsafe import Markup

class ListRadioWidget(object):

    def __init__(self, html_tag='ul', prefix_label=True):
        assert html_tag in ('ol', 'ul')
        self.html_tag = html_tag
        self.prefix_label = prefix_label

    def __call__(self, field, **kwargs):
        fname = 'ListRadioWidget - __call__'

        kwargs.setdefault('id', field.id)

        html = ['<div class="hover:bg-tblack-500">']

        for subfield in field:
            checked = ''
            checked_style = ''
            print(subfield.checked)
            if subfield.checked:
                checked = 'checked=True'
                checked_style = 'bg-tblack-500'
            
            radioButton = '''   <input type="radio" id="{subfield_id}" class="hover:bg-tblack-500" name="{subfield_name}" value="{subfield_data}" {checked}/> 
                                <label for="{subfield_id}" class="flex items-center cursor-pointer">
                                    <button class="w-4 h-4 inline-block mr-1 rounded-full border border-tblack-500 {{% if subfield.checked %}} bg-tblack-500 {{% endif %}}"></button>
                                Best choice</label>'''.format(
                                subfield_name = subfield.name,
                                subfield_id = subfield.id,
                                subfield_data = subfield.data,
                                checked = checked,
                                checked_style = checked_style
                                )

            html.append(radioButton)
        
        html.append('</div>')
        return Markup(''.join(html))
    
            

