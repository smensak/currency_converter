# currency_converter

## Description
Currency converter CLI application and web API application.

## Parameters
- `amount` - amount which we want to convert - float
- `input_currency` - input currency - 3 letters name or currency symbol
- `output_currency` - requested/output currency - 3 letters name or currency symbol

Parameter `output_currency` is optional, if not given application will convert input to all known currencies.

## Notes

 - please note that due to the fact that some currencies share same symbol, it may be necessary to use 3 letter code to specify desired currency
## Usage examples
### CLI 
```
./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK
```

### API
```
GET /currency_converter?amount=0.9&input_currency=¥&output_currency=AUD HTTP/1.1
```

## Supported currencies
It's possible to convert currencies listed below. Exchange rates are obtained form European Central Bank.

EUR Euro 					[€] \
USD	US dollar 				[$] \
AUD	Australian dollar	\
CAD	Canadian dollar		\
HKD	Hong Kong dollar	\
MXN	Mexican peso		\
NZD	New Zealand dollar	\
SGD	Singapore dollar	\
DKK	Danish krone 		\
ISK	Icelandic krona		\
NOK	Norwegian krone		\
SEK	Swedish krona 		\
JPY	Japanese yen 			[¥]\
CNY	Chinese yuan renminbi \
BGN	Bulgarian lev 			[лв]\
CZK	Czech koruna 			[Kč]\
GBP	Pound sterling 			[£]\
HUF	Hungarian forint 		[Ft]\
PLN	Polish zloty 			[zł]\
RON	Romanian leu 			[lei]\
CHF	Swiss franc 		\
HRK	Croatian kuna			[kn]\
RUB	Russian rouble			[₽]\
BRL	Brazilian real			[R$]\
IDR	Indonesian rupiah		[Rp]\
ILS	Israeli shekel			[₪]\
KRW	South Korean won		[₩]\
INR	Indian rupee		\
TRY	Turkish lira		\
MYR	Malaysian ringgit		[RM]\
PHP	Philippine peso			[₱]\
THB	Thai baht				[฿]\
ZAR	South African rand		[R]
