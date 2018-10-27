import pandas as pd
import matplotlib.pyplot as plt

# Writing an iterator to load data in chunks (1)
print('Writing an iterator to load data in chunks (1)')
# Initialize reader object: df_reader
df_reader = pd.read_csv('world_ind_pop_data.csv', chunksize=10)

print('\nFIRST CHUNK:')
print(next(df_reader))
print('\nSECOND CHUNK:')
print(next(df_reader))

# Writing an iterator to load data in chunks (4)
print('\nWriting an iterator to load data in chunks (4):\n')
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('world_ind_pop_data.csv', chunksize=1000)

# Initialize empty DataFrame: data
data = pd.DataFrame()

# Iterate over each DataFrame chunks
for df_urb_pop in urb_pop_reader:

    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip( df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

    # Append DataFrame chunk to data: data
    data = data.append(df_pop_ceb)

# Plot urban population data
data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()
