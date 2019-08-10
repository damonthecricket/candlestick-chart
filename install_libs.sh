
mkdir libs


git clone https://github.com/damonthecricket/pyutils libs/pyutils


cat <<EOF > libs/__init__.py

__all__ = [
	"pyutils"
]
EOF
