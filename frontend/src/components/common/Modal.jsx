export default function Modal({
  open,
  children,
}) {
  if (!open) return null;

  return (
    <div className="fixed inset-0 bg-black/60 flex items-center justify-center z-50">
      <div className="bg-slate-800 rounded-2xl p-8 w-[500px]">
        {children}
      </div>
    </div>
  );
}