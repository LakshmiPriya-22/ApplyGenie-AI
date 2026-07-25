const QuickAction = ({
  title,
  icon,
  onClick,
}) => {
  return (
    <button
      onClick={onClick}
      className="bg-cyan-500 hover:bg-cyan-600 text-white rounded-xl p-5 shadow-md transition flex flex-col items-center justify-center gap-3"
    >

      <span className="text-4xl">
        {icon}
      </span>

      <span className="font-semibold">
        {title}
      </span>

    </button>
  );
};

export default QuickAction;