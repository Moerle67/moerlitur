class FormInput:
    label = ""
    type = ""
    required = True
    readonly = False
    disabled = False
    def __init__(self, label, value="", type="text", required = "True", disabled=False, readonly=False, submit=False):
        self.label = label
        self.value = value
        self.type = type
        self.required = required
        self.disabled = disabled
        self.readonly = readonly
        self.submit = submit

    def __str__(self):
        antwort = '<label for="'+self.label+'">'+self.label+'</label>\n'
        antwort += '<input '
        if self.submit:
            antwort+= ' onchange="this.form.submit()" '
        antwort += 'type="'+self.type+'" class="form-control" id="'+self.label+'" value="'+self.value
        antwort += '" name="'+self.label+'"'
        if self.required: 
            antwort += " required"
        if self.readonly:
            antwort += " readonly"
        if self.disabled:
            antwort += " disabled"
        antwort += '>\n'
        return antwort

class FormSlider:
    label = ""
    min = 0
    max = 10
    required = True
    readonly = False
    marks = True

    def __init__(self, label, value="0", required = "True", min=0, max=10, marks = True):
        self.label = label
        self.value = value
        self.min = min
        self.max = max
        self.required = required
        self.marks = marks
    def __str__(self):
        antwort = '<label for="'+self.label+'">'+self.label+'</label>\n'
        antwort += '<input type="range" class="form-control-range" id="'+self.label+'" value="'+str(self.value)
        antwort += '" name="'+self.label+'"'
        antwort += ' min="'+str(self.min)+'"'
        antwort += ' max="'+str(self.max)+'"'
        if self.marks:
            antwort += ' list="range'+self.label+'"'
        if self.required: 
            antwort += " required"
        if self.readonly:
            antwort += " readonly"
        antwort += '>\n'
        if self.marks:
            antwort += '<datalist id="range'+self.label+'">'
            for i in range(self.min, self.max+1):
                antwort += '<option value="'+str(i)+'" label="'+str(i)+'"></option>'
            antwort += '</datalist>'
        return antwort


class FormAuswahl:
    liste = ""
    value = ""
    name = ""
    def __init__(self, name, daten, value=0, aktiv=True, submit=False, label=True):
            self.submit = submit
            self.label = label
            self.daten = daten
            try:
                self.value = int(value)
            except:
                self.value = -1
            self.name = name
            self.aktiv = aktiv
    def __str__(self):
        antwort=""    
        if self.label:
            antwort = '\n<label for="'+self.name+'">'+self.name+': </label>\n'
        antwort += '<select '
        if self.submit:
            antwort+= ' onchange="this.form.submit()" '
        antwort += 'name="'+self.name+'" class="form-control">\n'
        for zeile in self.daten:
            antwort += '<option value="'+str(zeile.id)+'"'
            if zeile.id == self.value:
                antwort += "selected "
            antwort +='>'+str(zeile)+'</option>'
        antwort += '</select>\n'
        return antwort

class FormDatalist:
    liste = ""
    name = ""
    def __init__(self, name, daten, value="", aktiv=True, submit=False, label=True, funktion=""):
            self.submit = submit
            self.label = label
            self.daten = daten
            self.value = value
            self.name = name
            self.aktiv = aktiv
            self.funktion = funktion
    def __str__(self):
        antwort=""    
        if self.label:
            antwort = '\n<label for="'+self.name+'">'+self.name+': </label>\n'
        antwort += f'<input list="{self.name}" name="txt_{self.name}" id="txt_{self.name}"'
        if self.value != "":
            antwort += f' value="{self.value}"'
        antwort += '><datalist '
        antwort += f'id ="{self.name}"'
        if self.submit:
            antwort+= ' onchange="this.form.submit()" '
        antwort += 'name="'+self.name+'">\n'
        for zeile in self.daten:
            if self.funktion=="":
                antwort += f'<option value="{zeile}"'
            else:
                antwort += f'<option value="{self.funktion(zeile)}"'
            antwort +='>'
        antwort += '</datalist>\n'
        antwort += f"<input type='submit' name='button' value='{self.name}_Ok'>"
        return antwort

class FormBtn:
    name = ""
    label = ""
    color = ""
    onClick = ""
    modal = ""
    novaliade = False
    type = ""
    def __init__(self, name, label, color="primary", onClick="", modal="", formnovalidate=False, type="submit"):
        self.name = name
        self.label= label
        self.color = color
        self.onClick = onClick
        self.modal = modal
        self.novaliade = formnovalidate
        self.type = type
    def __str__(self):
        antwort ='<button class="btn btn-'+self.color+'" name="button" value="'+self.label+'" '
        antwort += 'type="'+self.type+'" '
        if self.onClick != "":
            antwort += ' onclick="'+self.onClick+'()" '
        if self.modal != "":
            antwort += 'data-toggle="modal" data-target="#'
            antwort += self.modal
            antwort += '" '
        if self.novaliade:
            antwort += " formnovalidate"
        antwort += ' >'
        antwort +=  self.name
        antwort +=  '</button>'
        return antwort
        
class FormBtnSave:
    name = "Speichern"
    def __str__(self):
        antwort ='<button type="submit" class="btn btn-primary" name="button" value="save">'
        antwort +=  self.name
        antwort +=  '</button>'
        return antwort

class FormBtnOk:
    name = "OK"
    def __str__(self):
        antwort ='<button type="submit" class="btn btn-primary" name="button" value="ok">'
        antwort +=  self.name
        antwort +=  '</button>'
        return antwort
        
class FormBtnCancel:
    name = "Abbruch"
    def __str__(self):
        antwort ='<button type="submit" class="btn btn-danger" name="button" value="cancel" formnovalidate>'
        antwort +=  self.name
        antwort +=  '</button>'
        return antwort

class FormBtnNext:
    name = "Speichern und Nächster"
    def __str__(self):
        antwort ='<button type="submit" class="btn btn-primary" name="button" value="next">'
        antwort +=  self.name
        antwort +=  '</button>'
        return antwort

class FormBtnRemove:
    name = "Löschen"
    def __str__(self):
        antwort ='<button type="submit" class="btn btn-danger" name="button" value="remove" formnovalidate>'
        antwort +=  self.name
        antwort +=  '</button>'
        return antwort

def formRow(*liste):
    antwort = '<div class="form-row">\n'
    for element in liste:
        antwort += '<div class="col">' 
        antwort += str(element)
        antwort += '</div>'
    antwort += '\n</div>'
    return antwort

def formLinie():
    return "<hr />"