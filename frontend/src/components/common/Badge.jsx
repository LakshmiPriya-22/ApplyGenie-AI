export default function Badge({
  text,
}) {
  return (
    <span
      className="
      px-3
      py-1
      rounded-full
      bg-blue-600
      text-sm
      text-white
    "
    >
      {text}
    </span>
  );
}