# EOSPy

This project started with me challenging myself to mix coding (which I love) and Chemical Engineering (which I also love).
I hope to sometime soon work with a big Chemical Engineering software company developing their simulation software (think HYSYS, or UNISIM, or ChemCad.) 

This library is meant to be used as a tool to learn, I do not intend it to be used to design chemical plants or home experiments. 
It can be a fun and easy way to check your own hand calculations. 

## Equations of State in Library
  The EOS coded into this python program are based off [this website](http://www.ccl.net/cca/documents/dyoung/topics-orig/eq_state.html)
  and the book Introduction to Chemical Engineering Thermodynamics by Smith, Van Ness, and Abbott (sixth edition).
  
  The following are the EOS ready for use:
  
  The following are all the EOS being coded:
    1. Virial
    2. Reduced
    3. van der Waals
    4. Peng-Robinson
    
  The following are all the EOS being considered:
  
## Examples
  
  I have designed these functions to work with a list of compounds, one at a time. The following examples will be showing how to use 
  vanderWaals but all EOS can be used using the same structure.
  
  The first step is to create a list of strings of all the compounds you are interested in.
  
  ```
  from EOS.vanderWaals import vanderWaals
  
  compounds  = ['Acetic acid', 'Acetone', 'Benzene', 'Methane']
  ```
  
  The second step is to create a (insert EOS) object and call it whatever you want. For the following examples I will be using
  vanderWaals and I will call the object "vdW".
  ```
  vdW = vanderWaals('vdW')
 
  # Get compound data and store it in a variable called data. 
  
  data = vdW.get_data(compounds)
  
  # Print data in a human readable form using tabulate_data.
  
  vdW.tabulate_data(data)
  ```
  The function tabulate_data(a) prints the EOS object as a table using the tabulate python library. 
  tabulate_data converts the dictionary returned in every single on of the vdW function as a human-readable table such as the one below.
  
  ```
    Units are Kelvin,Pascals,and cubic meters/mol
  Compound     CAS_ID        Tc    Tc_Error       Pc    Pc_Error        Vc    Vc_Error
  -----------  --------  ------  ----------  -------  ----------  --------  ----------
  Acetic acid  64-19-7   593           2     5790000       30000  0.000171     2e-06
  Acetone      67-64-1   508.1         0.2   4700000      100000  0.000221     2e-05
  Benzene      71-43-2   562           0.1   4900000       20000  0.000257     1.1e-05
  Methane      74-82-8   190.56        0.02  4600000       10000  9.9e-05      3e-06
  ```
  We can now start to use the EOS formulas. First we will create variables to hold the value of our physical parameters.
  The units here are important, EOSPy uses Kelvin, Pascals, cubic meters, and moles.
  ```
  # Create variables to store the physical parameters. 
  t = 500
  p = 101325
  v = 0.1 
  n = 1
  ```
  Now we can create variables that hold the values that vdW will calculate for us. Now we can call tabulate_data() to 
  display our results.
  
  ```
  parameters = vdW.parameters(compounds)
  temperatures = vdW.temperature(compounds,p,n,v)
  pressures = vdW.pressure(compounds,t,n,v)

  vdW.tabulate_data(parameters)
  vdW.tabulate_data(temperatures)
  vdW.tabulate_data(pressures)
  ``` 
  The results are:
  ```
      Compound            a            b
    -----------  --------  -----------
    Acetic acid  1.77113   0.00010644
    Acetone      1.60185   0.000112352
    Benzene      1.87974   0.000119198
    Methane      0.230211  4.30529e-05
    
    Units are Kelvin,Pascals,and cubic meters/mol
    Compound       Temperature
    -----------  -------------
    Acetic acid        1219.53
    Acetone            1219.26
    Benzene            1219.51
    Methane            1218.46
    
    Units are Kelvin,Pascals,and cubic meters/mol
    Compound       Pressure
    -----------  ----------
    Acetic acid     41438
    Acetone         41457.4
    Benzene         41432.4
    Methane         41565.7
```
  
