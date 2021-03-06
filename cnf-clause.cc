/*  cnf-clause  Copyright (c) 2011, Vegard Nossum
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

extern "C" {
#include <stdio.h>
#include <stdlib.h>
}

#include "cnf.hh"

int main(int argc, char *argv[])
{
	cnf f;
	unsigned int max_nr_variables = 0;

	cnf::clause::ptr new_clause(new cnf::clause());
	for (int i = 1; i < argc; ++i) {
		/* XXX: error checking */
		int literal = atoi(argv[i]);
		if (literal == 0) {
			f.add(new_clause);
			new_clause = cnf::clause::ptr(new cnf::clause());
			continue;
		}

		new_clause->add(literal);

		unsigned int variable = literal < 0 ? -literal : literal;
		if (variable > max_nr_variables)
			max_nr_variables = variable;
	}

	f.print(stdout);
	return 0;
}
