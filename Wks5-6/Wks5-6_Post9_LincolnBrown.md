

```python
import pandas as pd
import re
```


```python
## This is a dirty dataset that needs to be cleaned
f = '5.-Jumbled-up-Customers-Details.xlsx'

df = pd.read_excel(f, engine='openpyxl', header=None)
```


```python
# As we can see, the columns are not properly extracted
# First thing we will do is remove those and leave commas in their place
headers = ["Name", "Address", "Age", "Gender"]
pattern = re.compile('(Name|Address|Age|Gender)')
clean_df = pd.DataFrame(columns=headers)
series = df[0]
for row in series:
    data = re.sub(pattern, ";", str(row))
    print(data)
    temp = data.lstrip().split(";")
    HTML(DataFrame(temp).to_html())
    del temp[0]
    out = dict(zip(headers, temp))
    clean_df = clean_df.append(out, ignore_index=True)

clean_df
```

    ; Hussein Hakeem ; Number 22 Fioye Crescent Surulere Lagos ; 17 ; Male
    ; Arojoye Samuel ; 11 Omolade Close Omole Estate Lagos ; 16 ; Male
    ; Alex Ezurum ; 1 Adamu Lane, Abuja ; 14 ; Male
    ; Susan Nwaimo ; Number 58 Yaba Street, Kaduna State  ; 16 ; Female
    ; Ajao Opeyemi ; No12 Olubunmi Street, Abeokuta ; 18 ; Female
    ; Banjoko Adebusola ; 34 Ngige Street, Ugheli, Delta ; 14 ; Female
    ; Muhammed Olabisi ; 13, ICAN road, Enugu ; 12 ; Female
    ; Oluwagbemi Mojisola ; ACCA Lane, Onitsha ; 13 ; Female





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Address</th>
      <th>Age</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Hussein Hakeem</td>
      <td>Number 22 Fioye Crescent Surulere Lagos</td>
      <td>17</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arojoye Samuel</td>
      <td>11 Omolade Close Omole Estate Lagos</td>
      <td>16</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Alex Ezurum</td>
      <td>1 Adamu Lane, Abuja</td>
      <td>14</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Susan Nwaimo</td>
      <td>Number 58 Yaba Street, Kaduna State</td>
      <td>16</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Ajao Opeyemi</td>
      <td>No12 Olubunmi Street, Abeokuta</td>
      <td>18</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Banjoko Adebusola</td>
      <td>34 Ngige Street, Ugheli, Delta</td>
      <td>14</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Muhammed Olabisi</td>
      <td>13, ICAN road, Enugu</td>
      <td>12</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Oluwagbemi Mojisola</td>
      <td>ACCA Lane, Onitsha</td>
      <td>13</td>
      <td>Female</td>
    </tr>
  </tbody>
</table>
</div>


