#!/usr/bin/python
# -*- coding: utf-8 -*-
# paczilla v0.8

# ---
# parse .csv files in a directory sequence for a specific column, 
# then merge and average results into a new .csv
#
#  HOW TO USE:
# add folders to script directory and run `python paczilla8.py`
# ---

import os

def paths():

    # assign values
    start_suffix = '--r1'
    end_suffix = '--r4.csv'
    file_suffix = '_summary.csv'
    my_dir = '.'

# ->|
    b = []
    # list all directories ending with start_suffix
    for d in os.listdir( my_dir ):
        if os.path.isdir( d ):
            if d.endswith( start_suffix ):
                b.append( d )

# ->|
    # for each directory listed in b[]
    for d in b:

        n = 1
        c = 0
        r0 = []; r1 = []; r2 = []; r3 = []; avg = []

        # create output filename
        output = d[:-4] + end_suffix 

        while c < 3:
            # if directory exists in sequence, open its directory
            d = d[:-1] + str( n )
            if os.path.exists( d ):
                for f in os.listdir( d ):

                    # for each file ending in file_suffix
                    if f.endswith( file_suffix ):
                        f = os.path.join( d,f )
                        with open( f,'r' ) as file:
                            #
                            for row in file:
                                if c == 0:
                                    name_column = row.split( ',' )[0]
                                    r0.append( name_column )
                                if n == 1:
                                    avg_column = row.split( ',' )[3]
                                    r1.append( avg_column )
                                    r1[0] = 'r' + str( n )
                                if n == 2:
                                    avg_column = row.split( ',' )[3]
                                    r2.append( avg_column )
                                    r2[0] = 'r' + str( n )
                                if n == 3:
                                    avg_column = row.split( ',' )[3]
                                    r3.append( avg_column )
                                    r3[0] = 'r' + str( n )
# --------->|
            else: pass

            n = n + 1
            c = c + 1

            if not r2 or not r3:
                pass
            else:                    
                a = 'avg'
                avg.append( a )
                for i in range( 1, len( r1 )):
                    a = float( r1[i] ) + float( r2[i] ) + float( r3[i] )
                    a = a / 3
                    avg.append( '%.6f' % a )

                open( output, 'w' ).close()
                for x in range( 0, len( r0 )):
                    m = open( output,'a' )
                    m.write( '%s,%s,%s,%s,%s\n' % ( r0[x],r1[x],r2[x],r3[x],avg[x] ))
                    m.close()

                print( '' )
                for x in range( 0, len( r0 )):
                    print( '%s,%s,%s,%s,%s' % ( r0[x],r1[x],r2[x],r3[x],avg[x] ))

if __name__ == "__main__":
    paths()


    
