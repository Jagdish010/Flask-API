# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def chess_board():
	row = ''
	for i in range(8):
		col = ''
		for j in range(8):
			c_color ='dark' if (i + j)% 2 == 0 else 'light'
			col += """<td class="chessboard" {} width='30px' height='30px'></td>""".format(c_color)
		
		row += """<tr class="chessboard">{}</tr>""".format(col)
	
	f = open('chess_board.html', 'w')
	f.write(wrapper() %(row))
	f.close()


def wrapper():
	return """<html>
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<meta http-equiv="X-UA-Compatible" content="ie=edge">
			<title>Checkerboard</title>

			<style>

				table.chessboard {
					margin: 80px auto;
					background: #999;
					border: 25px solid #333;
					border-collapse: collapse;
				}
				td.chessboard {
					border: 2px solid #333;
				}
				tr.chessboard:nth-child(odd) td.chessboard:nth-child(even),
				tr.chessboard:nth-child(even) td.chessboard:nth-child(odd) {
					background: white;
				}
			</style>
		</head>
		<body>
			<table class="chessboard" width='270px' height='270px'>%s</table>
		</body>
	</html>"""


if __name__ == '__main__':
	chess_board()