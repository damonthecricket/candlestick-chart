
mkdir libs


git clone https://github.com/damonthecricket/pyutils libs/pyutils
git pull https://github.com/damonthecricket/pyutils

git clone https://github.com/damonthecricket/pystock libs/pystock
git pull https://github.com/damonthecricket/pystock


cat <<EOF > libs/__init__.py

__all__ = [
	'pystock',
	'pyutils'
]
EOF
